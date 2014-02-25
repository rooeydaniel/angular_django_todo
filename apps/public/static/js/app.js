'use strict';

var todoApp = angular.module('todoApp', ['ngCookies', 'todoApp.controllers'])
    .run(function($http, $cookies) {
        $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
    });