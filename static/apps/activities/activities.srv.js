
(function(){
  angular.module('app')
    .factory('Activities', Tasks);

  Tasks.$inject = ['$http', '$resource', 'commonSrv'];

  function Tasks($http, $resource, commonSrv){
    var URL = '/api/status-logs/';
      var Task = $resource(URL + ':id/:sub/', {
        id:'@id',
      },{
        getpage: {method:'GET', sub:'?page=@page'},
      });
    return Task;
  }
})();

