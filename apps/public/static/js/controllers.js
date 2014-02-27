'use strict';

angular.module('todoApp.controllers', [])
    .controller('BaseController', ['$scope', '$window', 'Restangular', 'SessionService', function ($scope, $window, Restangular, SessionService) {
        var current_user = SessionService.getUserSession();
        if (current_user == null || current_user.user_id == null) {
            Restangular.one('user/id').get()
                .then(function (data) {
                    SessionService.saveUserSession(data[0]);
                });
        }

        $scope.doLogout = function () {
            SessionService.removeUserSession();
            $window.location = '/user/logout';
        };
    }])
    .controller('LoginController', ['$scope', function ($scope) {
        $scope.user = {}

        $scope.hasError = function (field, validation) {
            if (validation) {
                return $scope.loginForm[field].$dirty && scope.loginForm[field].$error[validation];
            }
            return $scope.loginForm[field].$dirty && $scope.loginForm[field].$invalid;
        };
    }])
    .controller('HomeController', ['$scope', function ($scope) {
        $scope.heading = 'Home Page';
    }])
    .controller('TodoController', ['$scope', '$http', 'Restangular', 'SessionService', function ($scope, $http, Restangular, SessionService) {
        $scope.todos = [];

        $scope.user = SessionService.getUserSession();

        Restangular.all('api/todos').customGET($scope.user.user_id)
            .then(function (data) {
                for (var i = 0; i < data.length; i++) {
                    $scope.todos.push(data[i].fields);
                }
            });

        $scope.addTodo = function (todo) {
            Restangular.all('api/todo/' + $scope.user.user_id).customPOST(todo)
                .then(function (data) {
                    $scope.todos = [];
                    for (var i = 0; i < data.length; i++) {
                        $scope.todos.push(data[i].fields);
                    }
                    $scope.todo.title = '';
                });
        }
    }]);