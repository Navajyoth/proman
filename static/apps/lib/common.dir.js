(function(){
    angular.module('app')
    .directive('busy', function(){
        return {
            restrict:'E',
            scope:{
                status: '=',
            },
            templateUrl: '/static/apps/templates/busy.html'
        };
    }) 
    .directive('loadMore', loadMore)
    .directive('autoFocus',['$timeout',autofocus])
    .directive('rdtDroppable', rdtDroppable)
    .directive('rdtDraggable', draggable);

    function rdtDroppable(){
        return{
            scope:{
                drop: '&',
            },
            link: linkFunction
        };

        function linkFunction(scope, element){
            var el = element[0];
            el.addEventListener( 'dragover',
                function(e) {
                    e.dataTransfer.dropEffect = 'move';
                    // allows us to drop
                    if (e.preventDefault) e.preventDefault();
                    this.classList.add('over');
                    return false;
                },
                false
            );
            el.addEventListener( 'dragenter',
                function(e) {
                    this.classList.add('over');
                    return false;
                },
                false
            );

            el.addEventListener( 'dragleave',
                function(e) {
                    this.classList.remove('over');
                    return false;
                },
                false
            );

            el.addEventListener( 'drop',
                function(e) {
                    // Stops some browsers from redirecting.
                    if (e.stopPropagation) e.stopPropagation();

                    this.classList.remove('over');

                    // var item = document.getElementById(e.dataTransfer.getData('Text'));
                    // console.log(item, e.dataTransfer);
                    // call the drop passed drop function
                    scope.$apply('drop()');
                    return false;
                },
                false
            );

        }
    }

    function draggable(){
        return {
            scope:{
                drag: '&',
            },
            link: linkFunction
        };

        function linkFunction(scope, element){
            // this gives us the native JS object
            var el = element[0];
            el.draggable = true;
            el.addEventListener(
                'dragstart',
                function(e) {
                    e.dataTransfer.effectAllowed = 'move';
                    e.dataTransfer.setData('Text', this.id);
                    this.classList.add('drag');
                    scope.$apply('drag()');
                    return false;
                },
                false
            );

            el.addEventListener(
                'dragend',
                function(e) {
                    this.classList.remove('drag');
                    return false;
                },
                false
            );
        }
    }

    function loadMore(){
        function ctrl($scope, $rootScope){
            $scope.busy = false;
            $scope.loadMore = function(){
                $scope.busy = true;
                $scope.$emit('loadMore');
            };
            $scope.$on('loaded', function(){
                $scope.busy = false;
            });
        }
        return{
            restrict: 'E',
            scope: {},
            controller: ctrl,
            template: '<a href="#" class="load-more btn btn-info" ng-click="loadMore()">Show More <i ng-hide="busy" class="fa fa-chevron-down"></i><i ng-show="busy" class="fa fa-refresh fa-spin"></i></a>'
        };
    };

    function autofocus ($timeout){
        return {
            restrict:'A',
            link:function(scope, $element){
                $timeout(function(){
                    $element[0].focus();
                });
            }
        };
    };

})();

