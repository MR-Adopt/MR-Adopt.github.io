package org.matsim.core.network;

import org.matsim.core.network.NetworkUtils;
import org.matsim.core.network.NetworkUtils.*;

import java.io.File;
import java.io.IOException;
import java.util.Collections;
import java.util.List;
import java.util.Map;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.io.TempDir;
import org.matsim.api.core.v01.Coord;
import org.matsim.api.core.v01.Id;
import org.matsim.api.core.v01.network.Link;
import org.matsim.api.core.v01.network.Network;
import org.matsim.api.core.v01.network.Node;
import org.matsim.core.network.io.MatsimNetworkReader;
import org.matsim.core.network.io.NetworkWriter;
import org.matsim.utils.objectattributes.attributeconverters.DisallowedNextLinksAttributeConverter;

public class DisallowedNextLinksTest_testNetworkWritingAndReading_GTTest {

	@TempDir
	public File tempFolder;

	public static Network n;

	@BeforeAll
	public static void createNetwork() {
		// Nodes
		//             n3
		// n0 --- n1 <    > n4 --- n5
		//             n2
		// Links
		//              l2 - * - l5
		// * - l0 - * <             > * - l4 - *
		//              l1 - * - l3
		n = NetworkUtils.createNetwork();
		Node n0 = NetworkUtils.createAndAddNode(n, Id.createNodeId("0"), new Coord(0, 0));
		Node n1 = NetworkUtils.createAndAddNode(n, Id.createNodeId("1"), new Coord(1, 0));
		Node n2 = NetworkUtils.createAndAddNode(n, Id.createNodeId("2"), new Coord(2, -1));
		Node n3 = NetworkUtils.createAndAddNode(n, Id.createNodeId("3"), new Coord(2, 1));
		Node n4 = NetworkUtils.createAndAddNode(n, Id.createNodeId("4"), new Coord(3, 0));
		Node n5 = NetworkUtils.createAndAddNode(n, Id.createNodeId("5"), new Coord(4, 0));
		NetworkUtils.createAndAddLink(n, Id.createLinkId("0"), n0, n1, Math.sqrt(2), 30 / 3.6, 900, 1);
		NetworkUtils.createAndAddLink(n, Id.createLinkId("1"), n1, n2, Math.sqrt(2), 30 / 3.6, 900, 1);
		NetworkUtils.createAndAddLink(n, Id.createLinkId("2"), n1, n3, Math.sqrt(2), 30 / 3.6, 900, 1);
		NetworkUtils.createAndAddLink(n, Id.createLinkId("3"), n2, n4, Math.sqrt(2), 30 / 3.6, 900, 1);
		NetworkUtils.createAndAddLink(n, Id.createLinkId("4"), n3, n4, Math.sqrt(2), 30 / 3.6, 900, 1);
		NetworkUtils.createAndAddLink(n, Id.createLinkId("5"), n4, n5, Math.sqrt(2), 30 / 3.6, 900, 1);
		// return n;
	}

	

// 	@Test
// 	void testNetworkWritingAndReading_h() throws IOException {
// 
// 		// Network n = createNetwork();
// 		Link l1 = n.getLinks().get(Id.createLinkId("1"));
// 
// 		DisallowedNextLinks dnl0 = NetworkUtils.getOrCreateDisallowedNextLinks(l1);
// 		dnl0.addDisallowedLinkSequence("car", List.of(l1.getId(), Id.createLinkId("2")));
// 
// 		File tempFile = new File(tempFolder, "network.xml");
// 		new NetworkWriter(n).write(tempFile.toString());
// 		Network network = NetworkUtils.createNetwork();
// 		new MatsimNetworkReader(network).readFile(tempFile.toString());
// 
// 		Link l2 = n.getLinks().get(Id.createLinkId("1"));
// 		DisallowedNextLinks dnl1 = NetworkUtils.getDisallowedNextLinks(l2);
// 		Assertions.assertEquals(dnl0, dnl1);
// 		Assertions.assertEquals(dnl0.hashCode(), dnl1.hashCode());
// 		Assertions.assertSame(l1.getId(), dnl1.getDisallowedLinkSequences("car").get(0).get(0));
// 	}
// 
// // 	public static Link inputTransformation_testNetworkWritingAndReading(Link l1) {		
// // 		// Network n = createNetwork();
// // 		Link l2 = n.getLinks().get(Id.createLinkId( l1.getId() ));
// //         return l2;
// // 	}
// // 
	@Test
	void testNetworkWritingAndReading_IT() throws IOException {

		// Network n = createNetwork();
		Link l1 = n.getLinks().get(Id.createLinkId("1"));
		
		DisallowedNextLinks dnl0 = NetworkUtils.getOrCreateDisallowedNextLinks(l1);
		dnl0.addDisallowedLinkSequence("car", List.of(l1.getId(), Id.createLinkId("2")));

		File tempFile = new File(tempFolder, "network.xml");
		new NetworkWriter(n).write(tempFile.toString());
		Network network = NetworkUtils.createNetwork();
		new MatsimNetworkReader(network).readFile(tempFile.toString());

		Link l2 = DisallowedNextLinksTest_testNetworkWritingAndReading_GT.inputTransformation_testNetworkWritingAndReading(l1);
		DisallowedNextLinks dnl1 = NetworkUtils.getDisallowedNextLinks(l2);
		Assertions.assertEquals(dnl0, dnl1);
		Assertions.assertEquals(dnl0.hashCode(), dnl1.hashCode());
		Assertions.assertSame(l1.getId(), dnl1.getDisallowedLinkSequences("car").get(0).get(0));
	}

}