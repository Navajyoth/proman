(function(){
  angular.module('app')
    .factory('Tasks', Tasks);

  Tasks.$inject = ['$http', '$resource', 'commonSrv'];

  function Tasks($http, $resource, commonSrv){
    var URL = '/api/tasks/';
      var Task = $resource(URL + ':id/:sub/', {
        id:'@id',
      },{
        update: {method:'PUT'},
        notify: {method:'GET', params:{id:'@id', sub:'notify'}},
      });
    return Task;
  }
})();

