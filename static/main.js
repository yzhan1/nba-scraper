/**
 * Created by yaomingzhan on 2017/8/5.
 */
(function () {
    'use strict';
    angular.module('HupuScraper', []).controller('ScraperController', ['$scope', '$log', '$http', '$timeout',
        function($scope, $log, $http, $timeout) {
            $scope.submitButtonText = '运行';
            $scope.loading = false;
            $scope.getResults = function () {
                // fire API request
                $http.post('/scrape', {}).success(function(results) {
                    $log.log(results);
                    getData(results);
                    $scope.news = null;
                    $scope.loading = true;
                    $scope.submitButtonText = '运行中';
                }).error(function (error) {
                    $log.log(error);
                });
            };

            function getData(jobID) {
                var timeout = '';
                var poller = function () {
                    $http.get('/results/'+jobID).success(function(data, status, headers, config) {
                        if(status === 202) {
                            $log.log(data, status);
                        } else if (status === 200){
                            $log.log(data);
                            $scope.loading = false;
                            $scope.submitButtonText = "运行";
                            $scope.news = data;
                            $log.log('set news to data');
                            $timeout.cancel(timeout);
                            window.location.reload();
                            return false;
                        }
                        timeout = $timeout(poller, 2000);
                    });
                };
                poller();
            }
        }
    ]);
}());