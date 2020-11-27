(ns exercism.bird-count-test
  (:require [clojure.test :refer [deftest testing is]]
            exercism.bird-count))

(deftest last-week-test
  (is (= [0 2 5 3 7 8 4] exercism.bird-count/last-week)))

(deftest today-test
  (testing "Today's bird count of disappointing week"
    (is (= 0 (exercism.bird-count/today [0 0 2 0 0 1 0]))))
  (testing "Today's bird count of busy week"
    (is (= 10 (exercism.bird-count/today [8 8 9 5 4 7 10])))))

(deftest increment-bird-test
  (testing "Increment today's count with no previous visits"
    (is (= [6 5 5 11 2 5 1] (exercism.bird-count/inc-bird [6 5 5 11 2 5 0]))))
  (testing "Increment today's count with multiple previous visits"
    (is (= [5 2 4 2 4 5 8] (exercism.bird-count/inc-bird [5 2 4 2 4 5 7])))))

(deftest day-without-birds-test
  (testing "Has day without birds with day without birds"
    (is (= true (exercism.bird-count/day-without-birds? [5 5 4 0 7 6 7]))))
  (testing "Has day without birds with no day without birds"
    (is (= false (exercism.bird-count/day-without-birds? [5 5 4 1 7 6 7])))))

(deftest n-days-count-test
  (testing "Count for first three days of disappointing week"
    (is (= 1 (exercism.bird-count/n-days-count [0, 0, 1, 0, 0, 1, 0] 3))))
  (testing "Count for first 6 days of busy week"
    (is (= 48 (exercism.bird-count/n-days-count [5, 9, 12, 6, 8, 8, 17] 6)))))

(deftest busy-days-test
  (testing "Busy days for disappointing week"
    (is (= 0 (exercism.bird-count/busy-days [1 1 1 0 0 0 0]))))
  (testing "Busy days for busy week"
    (is (= 5 (exercism.bird-count/busy-days [4 9 5 7 8 8 2])))))

(deftest odd-week-test
  (testing "Odd week for week matching odd pattern"
    (is (= true (exercism.bird-count/odd-week? [1 0 1 0 1 0 1]))))
  (testing "Odd week for week that does not match pattern"
    (is (= false (exercism.bird-count/odd-week? [2 2 1 0 1 1 1])))))