var app = angular.module('share_app',[]);

app.controller('FileListController', function($scope, $http, $interval){
	$scope.per_page = 10;
	$scope.page_no = 1;
	$scope.get_files = function(page_no, per_page){
		$http.post(
			'/files/myfiles/',
			{
				'responseType' : 'json',
				'params' : {
					'page_no' : page_no,
					'per_page':per_page,
					// 'search_text':$scope.searchText
					}
			}
			).success(function(data, status, headers, config){
				console.log(data);
				$scope.files = data.result;
				$scope.next_page = data.next;
				$scope.previous_page = data.previous;
				$scope.total_page = data.total_page;
				$scope.cur_page = data.cur_page;
				$scope.per_page = data.per_page;
			}).error(function(data, status, headers, config){
				alert("errors");
			});
	}
	$scope.get_files($scope.page_no, $scope.per_page);
	$scope.get_next_page = function(){
		$scope.get_files($scope.next_page, $scope.per_page)
	}
	$scope.get_previous_page = function(){
		$scope.get_files($scope.previous_page, $scope.per_page)
	}
	$scope.genRecords = function(){
		$scope.get_files($scope.cur_page, $scope.per_page)
	}
	$scope.share = function(file_id){
		$scope.file_id = file_id;
		$("#myModal").modal('show');
	}
});