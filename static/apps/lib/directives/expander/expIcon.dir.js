(function(){
    angular.module('app')
    .directive('expIcon', expIcon);

    function expIcon(){
        return{
            restrict: 'E',
            scope: {
                status: '='
            },
            link: linkFunction,
            templateUrl: 'static/apps/lib/directives/expander/expIcon.html'
        };

        function linkFunction(scope, element){

        }
    }
})();
