var app = angular.module('main', ['ngRoute']);
// var cors = require('cors');

// app.use(cors());

let base_url = function(){
	return window.location;
} ;


app.config(function($routeProvider, $locationProvider) {
	$routeProvider.when('/', {
		templateUrl: './components/home.html',
		controller: 'homeCtrl'
	}).when('/logout', {
		resolve: {
			deadResolve: function($location, user) {
				user.clearData();
				$location.path('/');
			}
		}
	}).when('/register', {
		templateUrl: './components/register.html',
		controller: 'registerCtrl'
	}).when('/login', {
		templateUrl: './components/login.html',
		controller: 'loginCtrl'
	}).when('/dashboard', {
		resolve: {
			check: function($location, user) {
				if(!user.isUserLoggedIn()) {
					$location.path('/login');
				}
			},
		},
		templateUrl: './components/dashboard.html',
		controller: 'dashboardCtrl'
	})
	.otherwise({
		template: '404'
	});

	$locationProvider.html5Mode(true);
});

app.service('user', function() {
	var userToken;
	var loggedin = false;

	this.getName = function() {
		return userToken;
	};

	this.setID = function(userID) {
		id = userID;
	};
	this.getID = function() {
		return id;
	};

	this.isUserLoggedIn = function() {
		if(!!localStorage.getItem('login')) {
			loggedin = true;
			var data = JSON.parse(localStorage.getItem('login'));
			console.log('loggedin user ', data);
			Token = data.Token;
		}
		return loggedin;
	};

	this.saveData = function(data) {
		console.log('save data ', data);
		userToken = data;
		loggedin = true;
		localStorage.setItem('login', JSON.stringify({
			Token: userToken,
		}));
	};

	this.clearData = function() {
		console.log('clear data');
		localStorage.removeItem('login');
		userToken = "";

		loggedin = false;
	}
})

app.controller('homeCtrl', function($scope, user, $http, $location) {
	$scope.user = user.getName();
	$scope.isUserLoggedIn = user.isUserLoggedIn();
	$scope.getProduct = function() {
		$http({
			url: 'http://127.0.0.1:8000/product/list',
			method: 'GET',
			headers: {
				'Content-Type': 'application/json'
			},
		}).then(function getProductSuccess(response) {
			var products = response.data;
			$scope.products = products;
		}, function getProductError(error) {
			console.log('getProduct error ', error);
		})
	}

	$scope.productDetails = function(product_id) {
		console.log(user.getName());
		$http({
			url: 'http://127.0.0.1:8000/product/'+product_id,
			method: 'GET',
			headers: {
				'Content-Type': 'application/json'
			},
		}).then(function productDetailsSuccess(response) {
			console.log('productDetails success ', response);

		}, function productDetailsError(error) {
			console.log('productDetails error ', error);
		})
	}	

	$scope.goToLogin = function() {
		$location.path('/login');
	};

	$scope.register = function() {
		$location.path('/register');
	};

	$scope.logout = function() {
		$location.path('/logout');
	};
});


app.controller('registerCtrl', function($scope, user, $http, $location) {
	$scope.user = user.getName();
	$scope.isUserLoggedIn = user.isUserLoggedIn();

	$scope.register = function() {
		// user.clearData();
		var username = $scope.username;
		var first_name = $scope.first_name;
		var last_name = $scope.last_name;
		var password = $scope.password;
		var user_type = $scope.user_type;
		$http({
			url: 'http://127.0.0.1:8000/auth/register',
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			data: { 
				'username': username,
				'first_name': first_name,
				'last_name': last_name,
				'password':password,
				'user_type':user_type

			}
		}).then(function registerSuccess(response) {
			console.log('register ctrl ', response);
			if(response.status == 200) {
				console.log('register ', response.data.token);

				user.saveData(response.data.token);
				$location.path('');
			}
		}, function registerError(ErrorResponse){
			console.log('error ', ErrorResponse);
			if(ErrorResponse.status == 400){
				alert('invalid user.');
			}
		})
	}

	$scope.goToLogin = function() {
		$location.path('/login');
	};

	$scope.regiser = function() {
		$location.path('/register');
	};

	$scope.logout = function() {
		$location.path('/logout');
	};
});

app.controller('loginCtrl', function($scope, $http, $location, user) {
	$scope.login = function() {
		// user.clearData();
		var username = $scope.username;
		var password = $scope.password;
		$http({
			url: 'http://127.0.0.1:8000/auth/login/',
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			data: { 'username': username,'password':password}
		}).then(function loginSuccess(response) {
			console.log('login ctrl ', response);
			if(response.status == 200) {
				console.log('login ', response.data.token);

				user.saveData(response.data.token);
				$location.path('');
			}
		}, function loginError(ErrorResponse){
			console.log('error ', ErrorResponse);
			if(ErrorResponse.status == 400){
				alert('invalid user.');
			}
		})
	}
});

app.controller('dashboardCtrl', function($scope, user, $http, $location) {
	$scope.user = user.getName();
	console.log('user ', $scope.user );
	$scope.getProduct = function() {
		$http({
			url: 'http://127.0.0.1:8000/product/list',
			method: 'GET',
			headers: {
				'Content-Type': 'application/json'
			},
		}).then(function homeSuccess(response) {
			var products = response.data;
			$scope.products = products;
		}, function homeError(error) {
			console.log('product error ', error);
		})
	}

	$scope.goToLogin = function() {
		$location.path('/login');
	};
	$scope.regiser = function() {
		$location.path('/register');
	}

	$scope.logout = function() {
		$location.path('/logout');
	}
	
});