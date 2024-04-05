<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Atribut selectorlar bilan ishlash</title>
	<style>
    * {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
	font-family: Arial;
}

.container {
	width: 100%;
	height: 100vh;
	background: url("https://raw.githubusercontent.com/diyorbek-ravshanqulov/diyorbek-ravshanqulov.github.io/main/18-dars_CSS/bg.jpg") no-repeat center;
	background-size: cover;
	display: flex;
	justify-content: center;
	align-items: center;
	animation: animateBG 5s linear infinite;
}

@keyframes animateBG {
	100% {
		filter: hue-rotate(360deg);
	}
}

form {
	width: 300px;
	height: 350px;
	border: 1px solid #ccc;
	border-radius: 10px;
	padding: 10px;
	backdrop-filter: blur(15px);
}

h2.title {
	text-align: center;
	text-transform: uppercase;
	color: white;
	margin: 10px auto;
	margin-bottom: 30px;
}

input {
	width: 100%;
	padding: 10px 15px;
	border: 2px solid #ccc;
	margin: 15px auto;
	outline: none;
	transition: all 0.3s;
	background-color: transparent;
	color: white;
}

input::placeholder {
	color: white;
	text-transform: capitalize;
}

input:focus {
	border-radius: 100px;
	border-color: yellow;
}

	/* input[type="text"] */
	/* input[type="password"] */
	/* input[type="submit"] */

input[type="submit"] {
	width: 200px;
	display: block;
	margin: 15px auto;
	border: none;
	background-color: rgba(0, 0, 255, 0.5);
	border-radius: 100px;
	cursor: pointer;
	text-transform: uppercase;
	text-align: center;
	font-weight: bold;
} 
input[type="submit"]:hover {
	background-color: dodgerblue;
	box-shadow: 0 0 5px rgba(0, 0, 255, 0.4);
}

a {
	border-color: white;
	height: 40px;
	position: absolute;
	bottom: 50px;
	width: 200px;
	display: block;
	border-radius: 100px;
	border: 2px solid #fff;
	text-decoration: none;
	padding: 2px 10px;
}
a:focus {
	border-color: yellow;
}

h6 {
	display: inline;
	font-size: 1.5em;
}
p {
	display: inline;
	font-size: 1em;
	color: white;
}
  </style>
</head>
<body>

	<div class="container">
		<form>
			<h2 class="title">Login Form</h2>
			<input type="text" placeholder="username">
			<input type="password" placeholder="password">
			<input type="submit" value="Login">
		</form>
		<a href="https://t.me/Diyorbek_Ravshanqulov" target="_blank"><p>Power by <h6>Diyorbek</h6></p></a>
	</div>

</body>
</html>
