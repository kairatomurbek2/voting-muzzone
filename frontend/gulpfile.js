var gulp = require('gulp'),
  plumber = require('gulp-plumber'),
  cleanCss = require('gulp-clean-css'),
  sass = require('gulp-sass'),
  autoprefixer = require('gulp-autoprefixer')

var css = {
  from: './css/*.scss',
  to: './css/',
  components: './css/**/*.scss'
}

gulp.task('css', () => {
  return gulp.src(css.from)
    .pipe(plumber())
    .pipe(sass())
    .pipe(autoprefixer())
    // .pipe(cleanCss())
    .pipe(gulp.dest(css.to))
});

gulp.task('watch:css', () => {
  gulp.watch([css.components], () => {
    gulp.start('css');
  })
})

gulp.task('watch', () => {
  gulp.start('watch:css');
})