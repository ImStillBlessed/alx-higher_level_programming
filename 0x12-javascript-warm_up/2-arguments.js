#!/usr/bin/node
const { argv } = require('node:process');
if (argv > 1)
  ? console.log('Argument found')
  : console.log('No argument')
