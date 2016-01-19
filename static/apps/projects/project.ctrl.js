(function(){
    angular.module('app')
    .filter('statusFilter', statusFilter)
    .controller('ProjectCtrl', ProjectCtrl)

    ProjectCtrl.$inject = ['$scope', '$stateParams', '$state', 'Tasks', 'commonSrv', 'toastr', 'tasks','$modal','constants','Users'];

    function ProjectCtrl($scope, $stateParams, $state, Tasks, commonSrv, toastr, tasks,$modal,constants,Users){
        var vm = this;

        init();

        function init(){
            vm.statusOptions = ['backlog', 'progress', 'rework', 'review', 'complete'];
            vm.tasks = tasks;
        }

        $scope.projectId = $stateParams.projectId;

        document.onkeypress = function(e){
            var inputFields = ['INPUT','TEXTAREA', 'DIV'];
            if((String.fromCharCode(e.charCode)==='n'||String.fromCharCode(e.charCode)==='N')
               &&(inputFields.indexOf(e.target.tagName.toUpperCase())==-1)){
                   vm.addTaskModal();
               }
        };

        vm.addTaskModal = function () {
            var newTask = {
                project: $scope.projectId
            }
            vm.tasks.unshift(newTask);
            var modalInstance = $modal({
                templateUrl: '/static/apps/tasks/html/edit.task.html',
                controller: 'UpsertTaskCtrl',
                resolve: {
                    task: function (){
                        return newTask;
                    }
                }
            });
        };
    }

    function statusFilter(){
        return function(tasks, status){
            return _.filter(tasks, function(task){
                return task.status===status;
            });
        };
    }
})();



