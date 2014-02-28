'use strict';

angular.module('todoApp.filters', [])
    .filter('todoFilter', function () {
        return function (items, types) {
            var filtered = [];

            angular.forEach(items, function (item) {
                if (types.completed == false) {
                    if (item.completed == false) {
                        filtered.push(item);
                    }
                } else {
                    filtered.push(item);
                }
            });

            return filtered;
        };
    })
    .filter('todoSearchFilter', function () {
        return function (items, searchText) {
            var filtered = [];

            angular.forEach(items, function (item) {
                if (searchText != '' && searchText != undefined) {
                    if (item.title.indexOf(searchText) != -1 || item.description.indexOf(searchText) != -1) {
                        filtered.push(item);
                    }
                } else {
                    filtered.push(item);
                }
            });

            return filtered;
        };
    });