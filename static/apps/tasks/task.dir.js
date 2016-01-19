(function(){
    angular.module('app')
    .directive('task', ['Tasks', 'Users', 'commonSrv', 'toastr', '$modal', 'constants', taskSummary]);

    function taskSummary(Tasks, Users, commonSrv, toastr, $modal, constants){
        return {
            restrict: 'E',
            templateUrl: '/static/apps/tasks/html/task.html',
            scope: {
                task:'=',
                index:'=',
                showProject:'@',
                showFooter:'@',
                showStatus:'@',
                showUser:'@',
                isManager:'@',
                showNotify:'=',
            },
            link: function (scope, element, attrs){
                scope.times = ['estimated_time', 'actual_time', 'rework_time'];
                scope.colors = ['#112233', '#19f', '#e95', '#F1C40F', '#27AE60', '#C0392B', '#F39C12', '#112233', '#112233', '#112233', '#112233', '#112233', ];
                scope.taskHrcy = {
                    backlog: {
                        next: 'progress',
                        // timeField: 'estimated_time',
                        // timeText: 'Self Estimate'
                    },
                    rework:{
                        next: 'review',
                        timeField: 'rework_time',
                        timeText: 'Rework Time'
                    },
                    progress:{
                        next: 'review', prev: 'backlog',
                        timeField: 'actual_time',
                        timeText: 'Time Taken',
                        validate: validateProgress
                    },
                    review:{
                        next: 'complete', prev: 'rework',
                        validate: validateReview,
                    },
                    complete:{
                        prev:'rework', next:'archive',
                    }
                };

                scope.edit = function(task){
                    $modal({
                        templateUrl: '/static/apps/tasks/html/edit.task.html',
                        controller: 'UpsertTaskCtrl',
                        backdrop: 'static',
                        resolve: {
                            task: function (){
                                return scope.task;
                            }
                        }
                    });
                };

                init();
                function init(){
                    scope.showDelete = scope.isManager;
                    scope.editTs =  !Boolean(scope.task.id);
                    scope.tags = scope.task.tag? scope.task.tag.split(',') : [];
                }

                scope.move = function(dir){
                    var statusInfo = scope.taskHrcy[scope.task.status];
                    var newStateInfo = scope.taskHrcy[statusInfo[dir]];
                    if(newStateInfo && newStateInfo.validate){
                        if(!newStateInfo.validate()){
                            return;
                        }
                    }
                    scope.task.status = statusInfo[dir];
                    update();
                };

                function validateReview(task){
                    // review validation removed temporary
                    // TODO add validation
                    return true;
                }

                function validateProgress(){
                    if(!scope.task.user){
                        toastr.error('Cannot move to progress without user');
                        return false;
                    }
                    return true
                }

                scope.notify = function(){
                    var task = new Tasks(scope.task);
                    task.$notify(function(){
                        toastr.info('Notification send for ' + scope.task.title);
                    }, commonSrv.handleError);
                };

                function update(){
                    toastr.info('Updating Task...');
                    scope.task.items = scope.task.items || [];
                    var task = new Tasks(scope.task);
                    task.$update(function(){
                        toastr.success('Updated task');
                    }, commonSrv.handleError);
                };
            }
        };
    }
})();

