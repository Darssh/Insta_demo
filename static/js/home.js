(function(){
	'use strict';

	angular.module('instagram.demo', ['ngRoute'])
		.controller('InstagramController',
			['$scope','$http', InstagramController]);

	function InstagramController($scope, $http) {
		$scope.add = function () {
			
		}
	}
})();