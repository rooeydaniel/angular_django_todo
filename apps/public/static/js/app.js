'use strict';

var todoApp = angular.module('todoApp', ['ngCookies', 'restangular', 'xeditable', 'todoApp.controllers', 'todoApp.services', 'todoApp.filters'])
    .config(['RestangularProvider', function (RestangularProvider) {
        RestangularProvider.setBaseUrl('http://localhost:8000');
    }])
    .run(function ($http, $cookies, editableOptions, editableThemes) {
        $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];

        editableOptions.theme = 'bs3';
        editableThemes.bs3.inputClass = 'input-sm';
        editableThemes.bs3.buttonsClass = 'btn-sm';

        toastr.options = {
            "positionClass": "toast-top-center"
        };
    });
