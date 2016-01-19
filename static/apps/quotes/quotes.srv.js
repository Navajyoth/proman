(function(){
  angular.module('app')
  .factory('Quotes', Quotes);

  Quotes.$inject = ['$http', '$resource', 'commonSrv', '$q'];

  function Quotes($http, $resource, commonSrv, $q){
    var URL = '/api/quotes/random/';
    var Quotes = $resource(URL);
    return Quotes;
  }
})();
