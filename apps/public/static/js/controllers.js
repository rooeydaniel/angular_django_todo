'use strict';

angular.module('todoApp.controllers', [])
    .controller('HomeController', ['$scope', '$http', function($scope, $http) {
        $scope.todos = [];

        $http.get('/api/todos', {
            headers: {'Content-Type': undefined },
            transformRequest: angular.identity
        }).success(function (data) {
			$scope.todos = data;
        }).error(function (response) {
        	console.log('Response: ' + response);
        });
    }]);