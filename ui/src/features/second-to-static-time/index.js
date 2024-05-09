export const timeInSecondsToStatic = (timeInSecond) => {
  let timeInStatic = '';
  if (timeInSecond < 60) {
    timeInStatic = 'few seconds ago';
  } else if (timeInSecond < 60 * 60) {
    timeInStatic = 'few minutes ago';
  } else if (timeInSecond < 24 * 60 * 60) {
    timeInStatic = 'few hours ago';
  } else if (timeInSecond < 7 * 24 * 60 * 60) {
    timeInStatic = 'few days ago';
  } else if (timeInSecond < 4 * 7 * 24 * 60 * 60) {
    timeInStatic = 'few weeks ago';
  } else if (timeInSecond < 12 * 4 * 7 * 24 * 60 * 60) {
    timeInStatic = 'few months ago';
  } else {
    timeInStatic = 'few years ago';
  }
  return timeInStatic;
};
