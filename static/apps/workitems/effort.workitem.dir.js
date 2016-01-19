(function(){
    angular.module('app')
    .directive('workitemEffort', workitemEffort);

    workitemEffort.$inject = ['$rootScope'];

    function workitemEffort($rootScope){
        return {
            restrict: 'E',
            scope: {
                workitem: "="
            },
            link: linkFunction,
            templateUrl: '/static/apps/workitems/html/effort.workitem.html'
        };

        function linkFunction(scope, attr, ele){
            scope.updateEffort = function(item, delta){
                item.effort = Number(item.effort) + Number(delta);
                item.$update(function(){
                    scope.$emit('effort-updated');
                });
            };
        }
    }
})();
