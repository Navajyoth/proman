(function(){
    angular.module('app')
    .controller('UpsertTaskCtrl', UpsertTaskCtrl);

    UpsertTaskCtrl.$inject = ['$scope', 'Tasks', 'Users', 'commonSrv', 'toastr', 'constants', '$modal', 'task', '$timeout', '$location'];

    function UpsertTaskCtrl($scope, Tasks, Users, commonSrv, toastr, constants, $modal, task, $timeout, $location){
        // task.items = JSON.parse(task.items);
        var orgTask;

        $scope.$watch('taskUser.user', function(value){
            if(value && (value.id != $scope.task.user)){
                $scope.task.user = value.id;
                $scope.task.user_name = value.name;
            } 
        },true);

        $scope.$watch('taskUser.reviewer', function(value){
            if(value && (value.id != $scope.task.reviewer)){
                $scope.task.reviewer = value.id;
            } 
        },true);

        //for managing task tech tags.
        $scope.$watch('tags.selected',function (value) {
            if(!$scope.task) return;
            if(!angular.equals($scope.tags.selected, undefined)){
                var tags = [];
                for(var index in $scope.tags.selected){
                    tags.push($scope.tags.selected[index].id);
                }
                $scope.task.tag = tags.join();
            }
        },true);

        function init(){
            $scope.tags = {
                all: angular.copy(constants.tags),
                selected: [],
            };
            $scope.editSubTask = [];
            $scope.priorityOpts = constants.priorityOpts;
            if(task.id){
                // click edit
                Tasks.get({id: task.id}, onTaskLoad);
            } else if($location.search().task) {
                Tasks.get({id: $location.search().task}, onTaskLoad);
            } else {
                onTaskLoad(task);
            }
        };

        function onTaskLoad(updated){
            $location.search('task', updated.id);
            $scope.task = _.extend(task || {}, updated);
            $scope.task.items = $scope.task.items || [];
            orgTask = angular.copy($scope.task);
            $scope.isEdit = {
                title: !$scope.task.id
            };
            Users.queryCached().then(function(users){
                $scope.users = users;
                $scope.taskUser = {};
                $scope.taskUser.user = _.findWhere(users, {id:$scope.task.user});
                $scope.taskUser.reviewer = _.findWhere(users, {id:$scope.task.reviewer});
            });
            // this code will handle the data from database (will bind back to the multi select)
            setTags();
            $scope.onItemsUpdate();
        }

        function setTags(){
            $scope.tags.selected= $scope.task.tag? function () {
                var tags = $scope.task.tag.split(',');
                var tagObjs = [];
                for(var key in tags){
                    tagObjs.push({id:tags[key]});
                }
                return tagObjs;
            }():[];
        }

        $scope.onItemBlur = function(item){
            item.edit = false;
            refreshItems();
        }

        function refreshItems(){
            $scope.task.items = _.filter($scope.task.items, function(i){
                return (i.name && i.name.length) || i.edit;
            });
        }

        $scope.addItem = function(){
            if($scope.task.items.length && $scope.task.items[$scope.task.items.length-1].name==''){
                return;
            }
            $scope.task.items.push({
                name: '',
                completed: false,
                edit:true,
            });
        };

        $scope.editItem = function(item){
            $scope.task.items.forEach(function(i){
                i.edit = false; 
            });
            item.edit = true;
        }

        $scope.onItemsUpdate = function(){
            // Move code execution to next cycle
            $timeout(refreshCompleted, 0);
            function refreshCompleted(){
                $scope.task.itemsCompleted = _.filter($scope.task.items, function(i){
                    return i.completed;
                });
            }
        }

        $scope.delete = function(hide){
            var confirmDelete = confirm('Are you sure you want to delete the task?');
            if(!confirmDelete) return;

            $scope.task.status = 'cancel';
            $scope.upsert(hide, onDelete,'Deleting Task...');
            function onDelete(){
                toastr.success('Deleted Task');
            }
        };

        $scope.upsert = function(hide){
            refreshItems();
            if($scope.task.id){
                update(hide);
            } else {
                create(hide);
            }
        }; 

        function create(hide){
            toastr.info('Creating Task...');
            var task = new Tasks($scope.task);
            task.$save(function(newTask){
                toastr.success('Created task');
                _.extend($scope.task, newTask);
            }, commonSrv.handleError);
            hide(); 
        };

        function update(hide){
            toastr.info('Updating Task...');
            var task = new Tasks($scope.task);
            task.$update(function(latest){
                $scope.task = _.extend($scope.task, latest);
                toastr.success('Updated task');
            }, commonSrv.handleError);
            hide(); 
            $location.search('task', null);
        };

        $scope.cancel = function(hide){
            $location.search('task', null);
            _.extend($scope.task, orgTask);
            hide(); 
        };

        init();
    }
})();
