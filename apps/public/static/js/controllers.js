'use strict';

angular.module('todoApp.controllers', [])
    .controller('HomeController', ['$scope', '$http', function ($scope, $http) {
        $scope.todos = [];

        $http.get('/api/todos', {
            headers: {'Content-Type': undefined },
            transformRequest: angular.identity
        }).success(function (data) {
            for (var i = 0; i < data.length; i++) {
                $scope.todos.push(data[i].fields);
            }
        }).error(function (response) {
            console.log('Response: ' + response);
        });

        $scope.addTodo = function (todo) {
            var fd = new FormData();
            fd.append("todoTitle", todo.title);

            $http.post('/api/todo', fd, {
                headers: {'Content-Type': undefined },
                transformRequest: angular.identity
            }).success(function (data) {
                $scope.todos = [];
                for (var i = 0; i < data.length; i++) {
                    $scope.todos.push(data[i].fields);
                }
                $scope.todo.title = '';
            }).error(function (response) {
                console.log('Response: ' + response);
            });
        };
    }]);