var fs = require('fs');
fs.readFile('files.txt', function(error, contents) {
    if (error) {
		return console.log('Error reading file');
	}
	var files = contents.toString('UTF-8').split('\n').filter(function(x) {
		return x !== '';
	});
	var word_count = 0;
	var file_count = 0;
	files.map(function(file){
		fs.readFile(file, function(error, contents){
			if(error) {
				return console.log('Error reading file: ' + file);
			}
			word_count += contents.toString('UTF-8').split(' ').length;
			file_count += 1;
			if (file_count == files.length) {
				console.log('total number of words in all files: ' + word_count);
			}
		});
	});
});

