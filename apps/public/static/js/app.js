'use strict';

var todoApp = angular.module('todoApp', ['ngCookies', 'restangular', 'todoApp.controllers', 'todoApp.services'])
    .config(['RestangularProvider', function(RestangularProvider) {
        RestangularProvider.setBaseUrl('http://localhost:8000');
    }])
    .run(function($http, $cookies) {
        $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
    });