(function(){
    angular.module('app')
    .directive('addWork', addWork);

    function addWork(Workitems, $stateParams){
        return{
            restrict: 'E',
            scope: {
                parent: '=',
            },
            link: linkFunction,
            templateUrl: '/static/apps/workitems/html/add.workitem.html'
        };

        function linkFunction(scope, attr, ele){
            scope.add = function(){
                var workitem = {
                    workitem: scope.parent.id,
                    text: scope.name,
                    project: $stateParams.projectId,
                    effort: 0,
                    tags: [],
                };
                Workitems.save(workitem, function(updated){
                    scope.$emit('new-workitem', updated);
                });
                scope.name = '';
            };

        }
    }
})();
