module.exports = function(grunt) {
  grunt.initConfig ({
    sass: {
      dist: {
        options: {
          includePaths: require('node-bourbon').includePaths,
          includePaths: require('node-neat').includePaths
        },
        files: {
          'articles/static/articles/style.css' : 'sass/style.scss'
        }
      }
    },
    watch: {
      source: {
        files: ['sass/**/*.scss'],
        tasks: ['sass'],
      }
    }
  });
  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.registerTask('default', ['sass']);
};