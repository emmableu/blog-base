export const STORAGE_KEY = 'employee-auth'

// Do user authorization verify
export function checkAuth () {
    const auth = JSON.parse(localStorage.getItem(STORAGE_KEY))
    return auth && Object.keys(auth).length && auth.name === "鸭绿江大鲤鱼" && auth.password === "emma.wang.00.666"
}
