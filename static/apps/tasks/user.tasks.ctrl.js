(function(){
    angular.module('app')
    .filter('taskUserFilter', taskUserFilter)
    .filter('taskFilter', taskFilter)
    .controller('UsersTasksCtrl', UsersTasksCtrl)
    .controller('UserTasksCtrl', UserTasksCtrl);

    UserTasksCtrl.$inject = ['$scope', '$stateParams', '$location', 'Tasks', 'commonSrv', 'toastr', '$modal'];
    UsersTasksCtrl.$inject = ['$scope', '$stateParams', '$state', 'Tasks', 'Users', 'commonSrv', 'toastr', '$timeout','constants','Projects','$modal'];

    function UserTasksCtrl($scope, $stateParams, $location, Tasks, commonSrv, toastr, $modal){
        var vm = this;

        init();

        function init(){
            vm.statusOptions = ['backlog', 'progress', 'rework', 'review', ];
            if($stateParams.userId) vm.tasks = Tasks.query({
                user:$stateParams.userId,
                exclude:'archive,cancel'
            });
            else {
                vm.tasks = Tasks.query({current:true});
            }
            if($location.search().task)showTaskModal();
        }


        function showTaskModal(){
            $modal({
                templateUrl: '/static/apps/tasks/html/edit.task.html',
                controller: 'UpsertTaskCtrl',
                backdrop: 'static',
                resolve: {
                    task: function (){
                        return;
                    }
                }
            });
        }   

    }

    function UsersTasksCtrl($scope, $stateParams, $state, Tasks, Users, commonSrv, toastr, $timeout,constants,Projects,$modal){
        var vm = this;
        var dragTask;
        init();
        function init(){
            vm.users = Users.query();
            vm.tasks = Tasks.query({status:'backlog,progress,rework', detail:true});
            vm.tags = constants.tags;
            vm.projects = Projects.query();
            vm.filter = {};
        }

        $scope.edit = function(task){
            var modalInstance = $modal({
                templateUrl: '/static/apps/tasks/html/edit.task.html',
                controller: 'UpsertTaskCtrl',
                resolve: {
                    task: function (){
                        return task;
                    }
                }
            });
        };

        $scope.$watch(function(){return vm.tags;},function(){
            vm.filter.tags = [];//['Django','AngularJS'];
            for(var key in vm.tags){
                if(vm.tags[key].checked){
                    vm.filter.tags.push(vm.tags[key].id);
                }
            }
        },true);

        $scope.$watch(function(){return vm.projects;},function(){
            vm.filter.projects = [];//['Django','AngularJS'];
            for(var key in vm.projects){
                if(vm.projects[key].checked){
                    vm.filter.projects.push(vm.projects[key].id);
                }

            }

        },true);

        //for changing/assigning user on a task
        vm.setUser = function (user,task,oldTaks) {
            var index = vm.tasks.indexOf(oldTaks);
            vm.tasks.splice(index,1);
            // To tackle dropping on the same place
            if(task.user==user.id){
                return;
            }
            task.user = user.id?user.id:null;
            var Task = new Tasks(task);
            Task.$update(function(){
                var msg = user.id?'Task ' + task.title + ' assigned to ' + user.name:'Task ' + task.title + ' has been  unassigned ';
                toastr.success(msg);
            }, commonSrv.handleError);
        };

        vm.drapOptions = {
            accept: function(dragEl) {
                if ($scope.list1.length >= 2) {
                    return false;
                } else {
                    return true;
                }
            }
        }; 

    }

    function taskUserFilter(){
        return function(tasks, userId){
            return _.filter(tasks, function(task){
                return task.user==userId;
            });
        };
    }

    function taskFilter(){
        return function(tasks, filter){
            return _.filter(tasks, function(task){
                var taskTags = task.tag?task.tag.split(','):[];
                var tagsCount = 0;
                for(var key in filter.tags){
                    if(!angular.equals(taskTags.indexOf(filter.tags[key]),-1)){
                        tagsCount++;
                    }
                }
                var result =(tagsCount==filter.tags.length&&!(angular.equals(filter.projects.indexOf(task.project),-1)&&filter.projects.length));
                //console.log(result);
                return result;
            });
        };
    }

})();


