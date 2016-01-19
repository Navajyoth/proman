(function(){
    angular.module('app')
    .directive('projectMilestones', projectMilestones);

    projectMilestones.$inject = ['Milestones', '$stateParams', '$rootScope'];

    function projectMilestones(Milestones, $stateParams, $rootScope){
        return {
            restrict: 'E',
            scope: {
                workitems: '=',
            },
            link: linkFunction,
            templateUrl: '/static/apps/milestones/html/project.milestones.html',
        };

        function linkFunction(scope, elements, attrs){
            function init(){
                Milestones.query({project: $stateParams.projectId}, onLoad);
            }

            function onLoad(milestones){
                scope.milestones = milestones;
            }

            // function refreshWorkitems(){
            //     scope.filteredWorkitems = _.filter(function(){
            //         return i.item
            //     })
            // }

            scope.add = function(){
                var newData = {
                    name: scope.newMilestoneName,
                    project: $stateParams.projectId
                }
                Milestones.save(newData, function(milestone){
                    scope.milestones.push(milestone);
                });
                scope.newData = '';
            }

            scope.removeWorkitem = function(workitem){
                workitem.milestone = null;
                workitem.$update();
            }

            scope.addWorkitem = function(milestone){
                var workitem = _.find(scope.workitems, function(i){
                    return i.id === $rootScope.data.selectWorkitemId;
                });
                console.log(workitem, milestone);
                workitem.milestone = milestone.id;
                workitem.$update();
            }

            init();
        }
    }
})();

