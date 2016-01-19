(function(){
    angular.module('app')
    .directive('projectTags', projectTags);

    projectTags.$inject = ['Projects', '$stateParams'];

    function projectTags(Projects, $stateParams){
        return {
            restrict: 'E',
            link: linkFunction,
            templateUrl: '/static/apps/tags/html/project.tags.html',
        };

        function linkFunction(scope, elements, attrs){
            function init(){
                Projects.get({id: $stateParams.projectId}, onLoad);
            }

            function onLoad(project){
                scope.project = project;
                project.tags = project.tags || [];
            }

            scope.add = function(){
                scope.project.tags.push(scope.newTag);
                scope.project.$update();
            }

            init();
        }
    }
})();
