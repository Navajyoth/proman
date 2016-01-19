(function() {
    'use strict';
    angular
        .module('app')
        .controller('ActivitiesCtrl', ActivitiesCtrl);
    ActivitiesCtrl.$inject = ['$scope','Activities'];
    /* @ngInject */
    function ActivitiesCtrl($scope,Activities) {
        var vm = this;
        init();
        ////////////////
        function init() {
        	vm.page = 1;
        	vm.hideLoader = false;
        	var list = Activities.getpage({page:vm.page},function(data){
        		vm.activities = data.results;
        		vm.totalCount = data.count;
        		vm.hideLoader = true;
        	});
        }

        vm.loadMore = function(){
        	if(vm.totalCount==vm.activities.length){
        		vm.hideLoader = false;
        		return;
        	}

        	vm.page = vm.page+1;
        	Activities.getpage({page:vm.page},function(data){
        		vm.activities =	vm.activities.concat(data.results);
        	});
        };

    }
})();