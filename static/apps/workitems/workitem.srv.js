(function(){
  angular.module('app')
  .factory('Workitems', Workitems);

  Workitems.$inject = ['$http', '$resource', 'commonSrv'];

  function Workitems($http, $resource, commonSrv){
    var URL = '/api/workitems/';
    var Workitem = $resource(URL + ':id/:sub/', {
      id:'@id',
    },{
        update: {method:'PUT'},
    });
    return Workitem;
  }
})();
