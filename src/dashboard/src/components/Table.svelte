<script lang="ts">
	import token from '../stores/auth';
	import DataTable, { Head, Body, Row, Cell } from '@smui/data-table';
	import LinearProgress from '@smui/linear-progress';
	import Button from '@smui/button';

	export let items: any[] = [];
	export let loaded = false;

	async function deleteUav(id: number) {
		const res = await fetch(`http://localhost:8000/api/v1/uavs/${id}/`, {
			method: 'DELETE',
			headers: {
				Authorization: `Bearer ${$token}`
			}
		});

		location.reload();
	}
</script>

<DataTable table$aria-label="User list" style="width: 100%;">
	<Head>
		<Row>
			<Cell numeric>ID</Cell>
			<Cell>Name</Cell>
			<Cell>Category</Cell>
			<Cell>Company</Cell>
			<Cell>Brand</Cell>
			<Cell>Actions</Cell>
		</Row>
	</Head>
	<Body>
		{#each items as item (item.id)}
			<Row>
				<Cell numeric>{item.id}</Cell>
				<Cell>{item.name}</Cell>
				<Cell>{item.category}</Cell>
				<Cell>{item.company}</Cell>
				<Cell>{item.brand}</Cell>
				<Cell>
					<a href={`/uav/${item.id}`}>Edit</a>
					<Button on:click={() => deleteUav(item.id)}>Delete</Button>
				</Cell>
			</Row>
		{/each}
	</Body>

	<LinearProgress
		indeterminate
		bind:closed={loaded}
		aria-label="Data is being loaded..."
		slot="progress"
	/>
</DataTable>
