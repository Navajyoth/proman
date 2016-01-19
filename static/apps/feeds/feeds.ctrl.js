(function() {
    'use strict';
    angular
        .module('app')
        .filter('feedsFilter', feedsFilter)
        .controller('FeedsCtrl', FeedsCtrl);
    FeedsCtrl.$inject = ['$scope','Feeds','$modal','commonSrv','toastr','constants'];
    /* @ngInject */
    function FeedsCtrl($scope,Feeds,$modal,commonSrv,toastr,constants) {
        var vm = this;
        init();


        function init() {
            Feeds.query(function(feeds){
                vm.feeds = feeds;
            });
            vm.tags = constants.articleTags.map(function(tag){return {name:tag}});
            vm.filter={};
            vm.filter.tags = [];
        	// $scope.images = ['http://expandsuccess.org/admin/images/Articles.jpg','http://astrocodeschool.com/static/img/python-logo.png','http://i.dailymail.co.uk/i/pix/2013/11/03/article-2486855-192ACC5200000578-958_964x682.jpg','http://www.adamtornhill.com/Imgs/home2.jpg','http://lokeshdhakar.com/projects/lightbox2/images/image-4.jpg']
        }

        $scope.$watch(function(){return vm.tags;},function(){
          vm.filter.tags = [];//['Django','AngularJS'];
          for(var key in vm.tags){
            if(vm.tags[key].checked){
              vm.filter.tags.push(vm.tags[key].name);
            }
          }
        },true);

        vm.openModalForArticle = function(){
            $modal({scope:$scope,templateUrl:'/static/apps/feeds/html/modal.newfeed.html'});
        };

        document.onkeypress = function(e){
            var inputFields = ['INPUT','TEXTAREA'];
            if((String.fromCharCode(e.charCode)==='n'||String.fromCharCode(e.charCode)==='N')&&(inputFields.indexOf(e.target.tagName.toUpperCase())==-1)){
                vm.openModalForArticle();
            }
        };

        $scope.addArticle = function(article,hide){
            var feed = new Feeds(article);
            var msg = 'Adding article..';
                toastr.info(msg);
            feed.$update(function(newFeed){
                msg = 'Added new article..';
                    toastr.success(msg);
                vm.feeds.push(newFeed);
            },commonSrv.handleError);
            hide();
        };
                
    }

    function feedsFilter(){
        return function(feeds, filter){
          return _.filter(feeds, function(feed){
            var feedTags = (feed.tags?feed.tags.split(','):[]).map(function(item){
                return item.trim();
            });
            var tagsCount = 0;
            for(var key in filter.tags){
              if(!angular.equals(feedTags.indexOf(filter.tags[key].trim()),-1)){
                tagsCount++;
              }
            }
            var result =(tagsCount==filter.tags.length);
            //console.log(result);
            return result;
          });
        };
      }
})();