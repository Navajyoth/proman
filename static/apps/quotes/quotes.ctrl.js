(function(){
  angular.module('app')
  .controller('QuotesCtrl', QuotesCtrl);

  QuotesCtrl.$inject = ['$scope', '$stateParams', '$state', 'Quotes', 'commonSrv', 'toastr'];

  function QuotesCtrl($scope, $stateParams, $state, Quotes, commonSrv, toastr){
    var vm = this;
    vm.qoute = Quotes.get(function(){
    });
  }
})();