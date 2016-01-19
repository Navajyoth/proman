(function(){
  angular.module('app')
  .factory('Milestones', Milestones);

  Milestones.$inject = ['$http', '$resource', 'commonSrv'];

  function Milestones($http, $resource, commonSrv){
    var URL = '/api/milestones/';
    var Milestone = $resource(URL + ':id/:sub/', {
      id:'@id',
    },{
        update: {method:'PUT'},
    });
    return Milestone;
  }
})();
