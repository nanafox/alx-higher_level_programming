#!/usr/bin/node

// This script computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];

request(url, function (error, response) {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(response.body);
    const completedTasks = {};

    tasks.forEach((task) => {
      if (task.completed) {
        completedTasks[task.userId] = (completedTasks[task.userId] || 0) + 1;
      }
    });

    console.log(completedTasks);
  }
});
