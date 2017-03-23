var fs = require('fs');
new Promise(function(resolve, reject) {
    // first step: read the file, break into lines
    fs.readFile('files.txt', function(error, contents) {
        if (error) {
            return reject(error);
        }
        resolve(contents.toString('UTF-8').split('\n').filter(function(x) {
            return x !== '';
        }));
    });
}).then(function(files) {
    // second step: for each file, create a promise, that
    // will resolve with a word count of the file
    return new Promise(function(resolve, reject) {
        var promises = files.map(function(file) {
            return new Promise(function(resolve, reject) {
                fs.readFile(file, function(error, contents) {
                    if (error) {
                        return reject(error);
                    }
                    return resolve(contents.toString('UTF-8').split(' ').length);
                });
            });
        });
        resolve(promises);
    });
}).then(function(promises) {
    // step 3: wait for all promises to complete.
    // calculate the grand total of counts reported by each
    // promise
    return new Promise(function(resolve, reject) {
        Promise
            .all(promises)
            .then(function(results) {
                resolve(results.reduce(function(x, y) {
                    return x + y;
                }));
            }).catch(function(error) {
                console.error('error while fan in:' + error);
            });
    });
}).then(function(result) {
    console.log('total number of words in all files: ' + result);
}).catch(function(error) {
    console.log('something went wrong: ' + error);
});
