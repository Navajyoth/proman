(function(){
  angular.module('app')
    .factory('Feeds', Feeds);

  Feeds.$inject = ['$http', '$resource', 'commonSrv'];

  function Feeds($http, $resource, commonSrv){
    var URL = '/api/articles/';
      var Feed = $resource(URL + ':id', {
        id:'@id',
      },{
        update: {method:'POST'},
      });
    return Feed;
  }
})();

