export function sort(array) {
  let len = array.length;
  let i = 0;
  let j = 0;
  let tmp = 0;
  let low = 0;
  let high = 0;
  let mid = 0;
  let result = 0;
  // 赋予数组副本
  result = array.slice(0);
  for (i = 1; i < len; i += 1) {
    tmp = result[i];
    low = 0;
    high = i - 1;
    while (low <= high) {
      mid = parseInt((low + high) / 2, 10);
      if (tmp < result[mid]) high = mid - 1;
      else low = mid + 1;
    }
    for (j = i - 1; j >= high + 1; j--) {
      result[j + 1] = result[j];
    }
    result[j + 1] = tmp;
  }
  return result;
}

export function reverse(array) {
  let tmp = [];
  let len = array.length;
  for (let i = 0; i < len; i += 1) {
    tmp.push(array[i]);
  }
  for (let i = 0; i < len; i += 1) {
    array[i] = tmp[len - i - 1];
  }
  return array;
}

export function unique(array) {
  let tmp = [];
  let len = array.length;
  for (let i = 0; i < len; i += 1) {
    for (let j = i + 1; j < len; j += 1) {
      if (array[i] == array[j]) {
        tmp = [];
        for (let k = 0; k < j; k += 1) {
          tmp.push(array[k]);
        }
        for (let k = j; k < len - 1; k += 1) {
          tmp.push(array[k + 1]);
        }
        array = tmp;
        j = j - 1;
        len = len - 1;
      }
    }
  }
  return tmp;
}
