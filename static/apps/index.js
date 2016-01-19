(function(){
    Angular.createApp('app', ['ngDragDrop', 'cgBusy','dndLists','angularjs-dropdown-multiselect',
        'mgcrea.ngStrap','ngAnimate','wu.masonry',
        'angular-timeline','angular-inview', 
        'textAngular', 'ui.bootstrap.datetimepicker', 'xeditable',
        'angular-loading-bar', 'relativeDate', ])
    .config(function($provide) {
        // this demonstrates how to register a new tool and add it to the default toolbar
        $provide.decorator('taOptions', ['taRegisterTool', '$delegate', function(taRegisterTool, taOptions) { // $delegate is the taOptions we are decorating
            taOptions.toolbar = [
                ['bold', 'italics', 'underline', 'strikeThrough', 'ul', 'ol', 'insertLink']
            ];
            return taOptions;
        }]);
    })
    .run(function(editableOptions) {
      // editableOptions.theme = 'bs3'; // bootstrap3 theme. Can be also 'bs2', 'default'
    })
    .directive('ngEnter', function() {
        return function(scope, element, attrs) {
            element.bind("keydown keypress", function(event) {
                if(event.which === 13) {
                    scope.$apply(function(){
                        scope.$eval(attrs.ngEnter);
                    });
                    event.preventDefault();
                }
            });
        };
    })
    .directive('focusOn',function($timeout) {
    return {
        restrict : 'A',
        link : function($scope,$element,$attr) {
            $scope.$watch($attr.focusOn,function(_focusVal) {
                $timeout(function() {
                    _focusVal ? $element.focus() :
                        $element.blur();
                });
            });
        }
    }
    })
    .directive(
        'pageTitle', 
        ['$rootScope', '$timeout',
            function($rootScope, $timeout) {
                return {
                    link: function(scope, element) {
                        var listener = function(event, toState) {
                            if (toState.data && toState.data.title) title = toState.data.title + " | ProMan";
                            $timeout(function() {
                                element.text(title);
                            }, 0, false);
                        };
                        $rootScope.$on('$stateChangeSuccess', listener);
                    }
                };
            }
        ]);

})();
