// place files you want to import through the `$lib` alias in this folder.

export const toggleTheme = () => {
    let theme = localStorage.getItem("theme")

    if (!theme) {
        localStorage.theme = "light"
        return "light"
    }

    if (theme == "light") {
        localStorage.theme = "dark"
        document.documentElement.classList.add('dark')
        return "dark"
    } else {
        localStorage.theme = "light"
        document.documentElement.classList.remove("dark")
        return "light"
    }
}

