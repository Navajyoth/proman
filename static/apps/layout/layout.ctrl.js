(function(){
  angular.module('app')
  .controller('LayoutCtrl', LayoutCtrl);


LayoutCtrl.$inject = ['$scope', '$rootScope', 'Users', 'commonSrv', '$q', '$sce', '$state'];

function LayoutCtrl($scope, $rootScope, Users, commonSrv, $q, $sce, $state){
  var vm = this;

  init();
  function init(){
    vm.user = Users.get({id:'self'}, angular.noop, commonSrv.handleError);
    $scope.trustAsHtml = function (html) {
      return $sce.trustAsHtml(html);
    };

    $scope.gotoState = function(state,params){
      $state.go(state,params);
    };

    $scope.content = [
    {
      "text": "<i class=\"fa fa-fw fa-newspaper-o\"></i>&nbsp;Articles",
        "click": "gotoState('articles')"
    },
    {
      "text": "<i class=\"fa fa-fw fa-rocket\"></i>&nbsp;Projects",
      "click": "gotoState('projects')"
    },
    {
      "text": "<i class=\"fa fa-fw fa-tasks\"></i>&nbsp;My tasks",
      "click": "gotoState('home')"
    },
    {
      "text": "<i class=\"fa fa-fw fa-clock-o\"></i>&nbsp;Activities",
      "click": "gotoState('activities')"
    },
    {
      "divider": true
    },
    {
      "text": "<i class=\"fa fa-fw fa-sign-out\"></i>&nbsp;Logout",
      "href": "/logout/",
      "target": "_self"
    }
    ];

  }
}

})();
