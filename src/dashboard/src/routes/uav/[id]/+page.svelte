<script lang="ts">
	import Select, { Option } from '@smui/select';
	import { page } from '$app/stores';
	import { onMount } from 'svelte';
	import Button from '@smui/button';
	import Textfield from '@smui/textfield';
	import Card, { Content } from '@smui/card';
	import { browser } from '$app/environment';
	import token from '../../../stores/auth';
	import { goto } from '$app/navigation';

	if (browser && !$token) {
		goto('/login');
	}

	onMount(() => loadData());

	let uav = {
		name: '',
		year: '',
		company: '',
		brand: '',
		category: ''
	};

	async function loadData() {
		const res = await fetch(`http://localhost:8000/api/v1/uavs/${$page.params.id}/`, {
			method: 'GET',
			headers: {
				Authorization: `Bearer ${$token}`,
				'Content-Type': 'application/json'
			}
		});

		const data = await res.json();
		uav = data;
	}

	async function updateUAV() {
		const res = await fetch(`http://localhost:8000/api/v1/uavs/${$page.params.id}/`, {
			method: 'PATCH',
			headers: {
				Authorization: `Bearer ${$token}`,
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(uav)
		});

		await res.json();
		goto('/uav');
	}
</script>

<svelte:head>
	<name>Update the UAV</name>
</svelte:head>

<div class="card-display max-w-xs mx-auto">
	<div class="card-container">
		<h1 class="h3 mb-3 fw-normal text-center">Update the UAV</h1>

		<Card padded>
			<Textfield bind:value={uav.name} variant="outlined" label="Name" />
			<Textfield class="mt-4" bind:value={uav.year} variant="outlined" label="Year" />

			<Select class="mt-4" bind:value={uav.company} label="Company">
				<Option value="Baykar">Baykar</Option>
			</Select>

			<Select class="mt-4" bind:value={uav.brand} label="Brand">
				<Option value="Bayraktar TB2">Bayraktar TB2</Option>
				<Option value="Bayraktar TB3">Bayraktar TB3</Option>
				<Option value="Bayraktar Akıncı">Bayraktar Akıncı</Option>
				<Option value="Bayraktar DİHA">Bayraktar DİHA</Option>
				<Option value="Bayraktar Mini İHA">Bayraktar Mini İHA</Option>
			</Select>

			<Select class="mt-4" bind:value={uav.category} label="Category">
				<Option value="İHA0">İHA0</Option>
				<Option value="İHA1">İHA1</Option>
				<Option value="İHA2">İHA2</Option>
				<Option value="İHA3">İHA3</Option>
			</Select>

			<Button class="mt-4" on:click={updateUAV}>Update</Button>
		</Card>
	</div>
</div>
