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
            $window.location = '/logout';
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
        var baseTodo = Restangular.all('api/todo');

        baseTodo.customGETLIST($scope.user.user_id)
            .then(function(data) {
                reloadTodos(data);
            });

        $scope.addTodo = function (todo) {
            baseTodo.all($scope.user.user_id).customPOST(todo)
                .then(function (data) {
                    reloadTodos(data);
                    $scope.todo.title = '';
                    $scope.todo.description = '';
                });
        };

        $scope.changeCompleted = function (todo) {
            baseTodo.all($scope.user.user_id).customPUT(todo)
                .then(function (data) {
                    reloadTodos(data);
                });
        };

        $scope.changeTitle = function (title, id) {
            var todo = {
                "id": id,
                "user": $scope.user.user_id,
                "title": title
            }

            baseTodo.all($scope.user.user_id).customPUT(todo)
                .then(function (data) {
                    reloadTodos(data);
                });
        };

        $scope.changeDescription = function (description, id) {
            var todo = {
                "id": id,
                "user": $scope.user.user_id,
                "description": description
            }

            baseTodo.all($scope.user.user_id).customPUT(todo)
                .then(function (data) {
                    reloadTodos(data);
                    $scope.deleteButton = true;
                });
        };

        $scope.removeTodo = function (todo) {
            baseTodo.all($scope.user.user_id).remove(todo)
                .then(function(data) {
                    reloadTodos(data);
                });
        }

        $scope.deleteButton = null;

        $scope.confirm = function () {
            $scope.deleteButton = true;
        }

        $scope.cancelDelete = function () {
            $scope.deleteButton = false;
        }

        function reloadTodos(data) {
            $scope.todos = [];
            for (var i = 0; i < data.length; i++) {
                var todo = data[i].fields;
                todo['id'] = data[i].pk;
                if (!todo['description']) {
                    todo['description'] = 'Empty';
                }
                $scope.todos.push(todo);
            }
        }
    }]);