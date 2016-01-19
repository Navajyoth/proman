(function(){

  angular.module('app')
  .config(config);

  config.$inject = ['$stateProvider', '$urlRouterProvider'];

  function config($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise("/my-tasks/");
    $stateProvider
    .state('projects', {
      url: '/projects/',
      data: {title: 'Projects'},
      views:{
        'nav':{
          template: ' <div class="head">Projects</div>',
        },
        'main':{
          templateUrl: '/static/apps/projects/html/all.projects.html',
          controller: 'AllProjectsCtrl',
          controllerAs: 'allprj'
        }
      }
    })
    .state('home', {
      url: '/my-tasks/',
      data: {title: 'My Tasks'},
      views:{
        'nav':{
          templateUrl: '/static/apps/quotes/html/quotes.nav.html',
          controller:'QuotesCtrl',
          controllerAs:'quotes'
        },
        'main':{
          templateUrl: '/static/apps/tasks/html/user.tasks.html',
          controller: 'UserTasksCtrl',
          controllerAs: 'usrtsk'
        }
      }
    })
    .state('user', {
      url: '/users/:userId/tasks',
      data: {title: 'User Tasks'},
      views:{
        'nav':{
          templateUrl: '/static/apps/users/html/nav.users.html',
          controller: 'NavUsersCtrl',
          controllerAs: 'navu'
        },
        'main':{
          templateUrl: '/static/apps/tasks/html/user.tasks.html',
          controller: 'UserTasksCtrl',
          controllerAs: 'usrtsk'
        }
      }
    })
    .state('project-main', {
      url: '/project-main/:projectId',
      data: {title: 'Project'},
      views:{
        'nav':{
          templateUrl: '/static/apps/projects/html/nav.main.projects.html',
          controller: 'NavProjectsCtrl',
          controllerAs: 'navprj'
        },
        'main':{
          templateUrl: '/static/apps/projects/html/main.project.html',
          controller: 'MainProjectCtrl',
          controllerAs: 'mpctrl'
        }
      },
      resolve: {
        tasks: function(Tasks, $stateParams, commonSrv, $q){
          var defer = $q.defer();
          Tasks.query({
            project:$stateParams.projectId,
            exclude:'archive,cancel'
          }, function(tasks){
            defer.resolve(tasks);
          }, commonSrv.handleError);
          return defer.promise;
        },
      },
    })
    .state('project', {
      url: '/projects/:projectId',
      data: {title: 'Project'},
      views:{
        'nav':{
          templateUrl: '/static/apps/projects/html/nav.projects.html',
          controller: 'NavProjectsCtrl',
          controllerAs: 'navprj'
        },
        'main':{
          templateUrl: '/static/apps/projects/html/project.html',
          controller: 'ProjectCtrl',
          controllerAs: 'pctrl'
        }
      },
      resolve: {
        tasks: function(Tasks, $stateParams, commonSrv, $q){
          var defer = $q.defer();
          Tasks.query({
            project:$stateParams.projectId,
            exclude:'archive,cancel'
          }, function(tasks){
            defer.resolve(tasks);
          }, commonSrv.handleError);
          return defer.promise;
        },
      },
    })
    .state('usersTasks', {
      url: '/users-tasks/',
      data: {title: 'Users-Tasks'},
      views:{
        'nav':{
          template: ' <div class="head">Users-Tasks</div>',
        },
        'main':{
          templateUrl: '/static/apps/tasks/html/users.tasks.html',
          controller: 'UsersTasksCtrl',
          controllerAs: 'usrstsk'
        }
      }
    })
    .state('articles', {
      url: '/article-feed/',
      data: {title: 'Articles'},
      views:{
        'nav':{
          template: ' <div class="head">Articles</div>',
        },
        'main':{
          templateUrl: '/static/apps/feeds/html/feeds.html',
          controller: 'FeedsCtrl',
          controllerAs: 'feeds'
        }
      }
    })
    .state('activities', {
      url: '/activity-log/',
      data: {title: 'Activities'},
      views:{
        'nav':{
          template: ' <div class="head">Activities</div>',
        },
        'main':{
          templateUrl: '/static/apps/activities/html/activities.html',
          controller: 'ActivitiesCtrl',
          controllerAs: 'actvts'
        }
      }
    });
  }

})();
