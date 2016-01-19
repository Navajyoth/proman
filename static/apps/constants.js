(function(){
  angular.module('app')
  .constant("constants", {
    tags:(function(){
      return ['Angular', 'Django', 'Refact', 'DevOps', 'Android', 'Node'].map(function(item){
        return{
          id: item,
          label: item,
        }
      });
    })(),
    priorityOpts:['low', 'normal', 'high', 'urgent'],
    articleTags:['django', 'python', 'angular', 'angularjs', 'javascript', 'web', 'mobile', 'android']

  });
})();
