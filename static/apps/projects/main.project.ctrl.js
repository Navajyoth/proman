(function(){
  angular.module('app')
  .controller('MainProjectCtrl', MainProjectCtrl);

  MainProjectCtrl.$inject = ['$scope', '$rootScope', '$stateParams', '$state', 'Tasks', 'commonSrv', 'toastr', 'tasks','$modal','constants','Users', 'Workitems'];

  function MainProjectCtrl($scope, $rootScope, $stateParams, $state, Tasks, commonSrv, toastr, tasks, $modal, constants, Users, Workitems){
    var vm = this,
        projectId = $stateParams.projectId;

    function init(){
        Workitems.query({project: projectId}, function(items){
            vm.workitems = items;
        });
        $rootScope.sharedData = {
            hideEstimate: true
        };
        vm.projectId = projectId;
    }

    function refresh(){
        Workitems.query({project: projectId}, function(items){
            items.forEach(function(newItem){
                var old = _.find(vm.workitems, function(oldItem){
                    return newItem.id === oldItem.id
                });
                if(old){
                    _.extend(old, newItem);
                } else {
                    vm.workitems.push(newItem);
                }
            });
        });
    }

    $scope.$on('effort-updated', refresh);

    $scope.$on('new-workitem', function(event, item){
        vm.workitems.push(item);
    });

    init();
  }
})();




