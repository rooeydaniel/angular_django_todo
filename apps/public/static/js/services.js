'use strict';

angular.module('todoApp.services', ['angularLocalStorage'])
    .factory('SessionService', ['storage', function(storage) {
        return {
            saveUserSession: function(data) {
                storage.set('user', data);
            },
            getUserSession: function() {
                return storage.get('user');
            },
            removeUserSession: function() {
                storage.remove('user');
            }
        };
    }]);