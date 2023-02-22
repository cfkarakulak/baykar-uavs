<script>
	import { goto } from '$app/navigation';
	import { browser } from '$app/environment';
	import token from '../../stores/auth';

	if (browser && $token) {
		goto('/uav');
	}

	const credentials = {
		email: '',
		username: '',
		password: '',
		password2: ''
	};

	async function register() {
		await registerLocal(credentials);
	}

	async function registerLocal(credentials) {
		const res = await fetch('http://localhost:8000/api/v1/auth/register/', {
			method: 'POST',
			body: JSON.stringify({
				email: `${credentials.username}@gmail.com`,
				username: credentials.username,
				password: credentials.password,
				password2: credentials.password
			}),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (res.status == 201) {
			const res2 = await fetch('http://localhost:8000/api/v1/auth/token/', {
				method: 'POST',
				body: JSON.stringify({
					username: credentials.username,
					password: credentials.password
				}),
				headers: {
					'Content-Type': 'application/json'
				}
			});

			const data2 = await res2.json();

			if (data2.access) {
				token.set(data2.access);
				goto('/uav');
			}
		}
	}
</script>

<svelte:head>
	<title>Register</title>
</svelte:head>

{#if !$token}
	<form>
		<h1 class="h3 mb-3 fw-normal text-center">Please sign up</h1>

		<div class="w-full max-w-xs mx-auto">
			<form class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
				<div class="mb-4">
					<label class="block text-gray-700 text-sm font-bold mb-2" for="username">
						Username
					</label>
					<input
						bind:value={credentials.username}
						class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
						id="username"
						type="text"
						placeholder="Username"
					/>
				</div>

				<div>
					<label class="block text-gray-700 text-sm font-bold mb-2" for="password">
						Password
					</label>
					<input
						bind:value={credentials.password}
						class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
						id="password"
						type="password"
						placeholder="******************"
					/>
				</div>

				<div class="mb-6">
					<label class="block text-gray-700 text-sm font-bold mb-2" for="password">
						Confirm Password
					</label>
					<input
						bind:value={credentials.password2}
						class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
						id="password2"
						type="password"
						placeholder="******************"
					/>
				</div>

				<div class="flex items-center justify-between">
					<button
						class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
						on:click|preventDefault={register}
					>
						Sign Up
					</button>
				</div>
			</form>
		</div>
	</form>
{/if}
