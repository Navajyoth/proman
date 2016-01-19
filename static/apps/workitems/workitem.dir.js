(function(){
    angular.module('app')
    .directive('workitemsSummary', workitemsSummary)
    .directive('workitems', workitems);

    workitems.$inject = ['$compile', '$timeout', '$rootScope', 'Workitems'];
    workitemsSummary.$inject = ['$compile', '$timeout', '$rootScope', 'Workitems'];

    function baseWorkitem(scope){
        function init(){
            scope.data = {
                depth:  Number(scope.depth) + 1
            };

            scope.$watch('items.length', onItems);
        }

        scope.range = function(n){
            return _.range(0, n);
        };

        scope.save = function(l1){
            l1.$update();
        };

        function onItems(){
            if(scope.milestone){
                scope.filterdItems = _.filter(scope.items, function(i){
                    return i.milestone == scope.milestone;
                });
                console.log(scope.filterdItems);
                return;
            }
            scope.filterdItems = _.filter(scope.items, function(i){
                return i.workitem == scope.parent;
            });
        };

        scope.toggleStatus = function(item){
          item.status = (item.status==='completed')?'progress':'completed';
          item.$update();
        }

        init();
    }

    function workitemsSummary($compile, $timeout, $rootScope){
        return {
            restrict: 'E',
            scope: {
                items: '=',
                parent: '@',
                depth: '@',
                milestone: '@',
            },
            templateUrl: '/static/apps/workitems/html/summary.workitems.html',
            link: linkFunction,
        };
        function linkFunction(scope, element){
            baseWorkitem.call(this, scope);
            
            // Recursive method to create folder structure
            scope.addInner = function(item){
                // Give time for DOM to be created
                $timeout(onTimeout, 0);
                function onTimeout(){
                    if(!item) return;
                    var inner = $(element).find('#wi_' + item.id);
                    var dir = '<workitems-summary parent="' + item.id + '" items="items" depth="' + scope.data.depth + '"></workitems-summary>'
                    inner.append(dir);
                    $compile(inner)(scope);
                }   
            }
        }
    }

    function workitems($compile, $timeout, $rootScope){
        return {
            restrict: 'E',
            scope: {
                items: '=',
                parent: '@',
                depth: '@'
            },
            templateUrl: '/static/apps/workitems/html/workitems.html',
            link: linkFunction,
        };
        function linkFunction(scope, element, attrs){

            baseWorkitem.call(this, scope);

            scope.root = $rootScope.sharedData;
            scope.selectWorkitem = function(wi){
                $rootScope.data = $rootScope.data || {};
                $rootScope.data.selectWorkitemId = wi.id;
            };
            //
            // Recursive method to create folder structure
            scope.addInner = function(item){
                // Give time for DOM to be created
                $timeout(onTimeout, 0);
                function onTimeout(){
                    if(!item) return;
                    var inner = $(element).find('#wi_' + item.id);
                    var dir = '<workitems parent="' + item.id + '" items="items" depth="' + scope.data.depth + '"></workitems>'
                    inner.append(dir);
                    $compile(inner)(scope);
                }   
            }
        }
    }
})();
