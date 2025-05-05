// Get relative time between two dates
export function getRelativeTime(startDate: Date, endDate = new Date()) {
  const diffSeconds = Math.floor((endDate.getTime() - startDate.getTime()) / 1000)
  if (diffSeconds < 0) {
    return null
  }
  const diffMinutes = Math.floor(diffSeconds / 60)
  if (diffMinutes < 10) {
    return 'just now'
  }
  if (diffMinutes < 60) {
    return `${diffMinutes} minutes ago`
  }
  const diffHours = Math.floor(diffMinutes / 60)
  if (diffHours < 24) {
    return `${diffHours} hours ago`
  }
  const diffDays = Math.floor(diffHours / 24)
  if (diffDays < 10) {
    return `${diffDays} days ago`
  }
  return null
}

// Get a formatted date as: DD/MM/YYYY Day
export function getFormattedDate(date: Date) {
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()
  const weekday = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][
    date.getDay()
  ]

  return `${padZero(day)}/${padZero(month)}/${year} ${weekday}`
}

// Pad number with leading zeros
function padZero(number: number, len = 2) {
  return number.toString().padStart(len, '0')
}

// Get formatted date and time as: DD/MM/YYYY 12:00
export function getFormattedDateTime(date: Date) {
  const year = date.getFullYear()
  const month = padZero(date.getMonth() + 1)
  const day = padZero(date.getDate())
  const hours = padZero(date.getHours())
  const minutes = padZero(date.getMinutes())

  return `${day}/${month}/${year} ${hours}:${minutes}`
}

// Get difference in days between two dates
export function getDiffInDays(startDate: Date, endDate = new Date()) {
  return Math.floor((endDate.getTime() - startDate.getTime()) / (1000 * 86400))
}

// Get a short date format: DD/MM
export function getShortDate(date: Date) {
  const month = padZero(date.getMonth() + 1)
  const day = padZero(date.getDate())

  return `${day}/${month}`
}

// Get number of days in the year of a date
export function getDaysInYear(date: Date) {
  const year = date.getFullYear()
  if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
    return 366
  }
  return 365
}

// Get the start date of the year
export function getStartOfYear(date: Date) {
  const year = date.getFullYear()
  return new Date(year, 0, 1)
}

// Get the start of the day (midnight)
export function getStartOfDay(date: Date) {
  return new Date(date.getFullYear(), date.getMonth(), date.getDate())
}
